import axiosWithoutAuth from "@/axiosWithoutAuth";
import ModuleCard from "@/components/cards/ModuleUnionCard";
import Layout from "@/components/Layout";
import PageHeader from "@/components/PageHeader";
import Pagination from "@/components/Pagination";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import { GetServerSideProps } from "next";
import Link from "next/link";
import { FC } from "react";

interface PropositionsProps {
  propositionsData: any;
}

const Propositions: FC<PropositionsProps> = ({ propositionsData }: PropositionsProps) => {
  const propositions = propositionsData["results"] || [];
  const propositionCards = propositions.map((proposition) => (
    <Grid item key={proposition.slug} xs={6} sm={4} md={3}>
      <Link href={`/propositions/${proposition.slug}`}>
        <a>
          <ModuleCard module={proposition}>
            <div dangerouslySetInnerHTML={{ __html: proposition.summary }} />
          </ModuleCard>
        </a>
      </Link>
    </Grid>
  ));

  return (
    <Layout title={"Propositions"}>
      <Container>
        <PageHeader>Propositions</PageHeader>
        <Pagination count={propositionsData["total_pages"]} />
        <Grid container spacing={2}>
          {propositionCards}
        </Grid>
        <Pagination count={propositionsData["total_pages"]} />
      </Container>
    </Layout>
  );
};

export default Propositions;

// https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering
export const getServerSideProps: GetServerSideProps = async (context) => {
  let propositionsData = {};

  await axiosWithoutAuth
    .get("http://django:8000/api/propositions/", { params: context.query })
    .then((response) => {
      propositionsData = response.data;
    })
    .catch((error) => {
      // console.error(error);
    });

  return {
    props: {
      propositionsData,
    },
  };
};