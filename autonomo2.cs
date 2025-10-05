using System;
using System.IO;
using System.Text;

namespace autonomo2
{
   public class main_class
   {
      static System.Random random_generator = new System.Random();
      public static void Main(string[] args)
      {
         string raptor_prompt_variable_zzyz;
         ?? pc;
         ?? jugador;
      
         raptor_prompt_variable_zzyz ="Ingresa tu opción: piedra, papel o tijera";
         Console.WriteLine(raptor_prompt_variable_zzyz);
         jugador= Double.Parse(Console.ReadLine());
         if (jugador=="piedra")
         {
            pc =floor(random_generator.NextDouble()*3)+1;
            if (pc==1)
            {
               Console.WriteLine("Empate");
            }
            else
            {
            }
            if (pc==2)
            {
               Console.WriteLine("Perdiste");
            }
            else
            {
            }
            if (pc==3)
            {
               Console.WriteLine("Ganaste");
            }
            else
            {
            }
         }
         else
         {
         }
         if (jugador=="papel")
         {
            pc =floor(random_generator.NextDouble()*3)+1;
            if (pc==1)
            {
               Console.WriteLine("Ganaste");
            }
            else
            {
            }
            if (pc==2)
            {
               Console.WriteLine("Empate");
            }
            else
            {
            }
            if (pc==3)
            {
               Console.WriteLine("Perdiste");
            }
            else
            {
            }
         }
         else
         {
         }
         if (jugador=="tijera")
         {
            pc =floor(random_generator.NextDouble()*3)+1;
            if (pc==1)
            {
               Console.WriteLine("Perdiste");
            }
            else
            {
            }
            if (pc==2)
            {
               Console.WriteLine("Ganaste");
            }
            else
            {
            }
            if (pc==3)
            {
               Console.WriteLine("Empate");
            }
            else
            {
            }
         }
         else
         {
         }
      }
   }
}
